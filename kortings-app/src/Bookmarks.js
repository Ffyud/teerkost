import React, {useState, useEffect, Suspense} from "react";
import Offers from './offers.json';
import ShareDialog from "./ShareDialog";
import localForage from "localforage";
import NoBookmarks from "./NoBookmarks";
import CopyButton from "./CopyButton";

const ProductsContainer = React.lazy(() => import ('./ProductsContainer'));

function Bookmarks(props) {
  
  useEffect(() => {
    window.scrollTo(0, 0);
  });

  const [selectedOffers, setSelectedOffers] = useState([]);  
  const [bookmarkCount, setBookmarkCount] = useState(0);
  const [oldBookmarksExist, setOldBookmarksExist] = useState(false);


  useEffect(() => {
    var bookmarkedIds = undefined;
    
    localForage.getItem('teerkost-bookmarks').then(function (value) {
      if(value !== null) { // if something is present in browserstorage
        bookmarkedIds = value
        updateOfferListById(bookmarkedIds)
        checkIfOffersExist(bookmarkedIds)
        setBookmarkCount(bookmarkedIds.length)
      } else {
        console.info("Er staan geen bookmarks in deze browser opgeslagen.")
      }
    }).catch(function(err) {
        console.warn("Iets misgegaan bij het ophalen van de bookmarks: " + err)
    })
  }, [])

  const updateOfferListById = (bookmarkIdList) => {
    var productIdFilter = object => object.productId === null;

    if(bookmarkIdList !== null) {
      productIdFilter = object => bookmarkIdList.includes(object.productId);
      console.log("Filter voor lijst met bookmarks ingesteld.")
    }
    else {
      console.log("Geen bookmarkId array gevonden, dus niks.")
    }

    console.log("Totale aantal aanbiedingen: " + Offers.length)

    var filtered = Offers.filter(productIdFilter)
    
    setSelectedOffers(filtered);
    console.log("Aantal aanbiedingen na filter: " + filtered.length)
  }

  const checkIfOffersExist = (bookmarkedIds) => {
    var i = 0;
    bookmarkedIds.forEach((productId) => {
      var searchOffersResult = Offers.find(object => object.productId === productId);
      if(searchOffersResult === undefined) {
        console.log("Bookmark met het productId " + productId + " niet meer gevonden.")
        i = i + 1;

        localForage.getItem('teerkost-bookmarks').then(function (value) {
          if(value !== null) { // if something is present in browserstorage
            var allBookmarks = value;
            allBookmarks = allBookmarks.filter(element => element !== productId) // remove from existing array
            localForage.setItem('teerkost-bookmarks', allBookmarks).then(function(value) {
              console.log(productId + " is niet meer actueel en wordt verwijdert uit de bookmarks.")
              setOldBookmarksExist(true)
            }).catch(function (err) {
              console.log("Iets misgegaan bij het opslaan van bookmarks: " + err)
            })
          }
        });
      }
    }); 
  }

  const verlopenMelding = (exist) => {
    if(exist === false) {
      return "Er zijn niet actuele aanbiedingen verwijdert."
    } else {
      return ""
    }
  }

  return (
    <div className="app-wrap">
        <a className="title-sober" href='https://teerkost.nl'><span>Teerkost</span></a>
        { selectedOffers.length > 0  ? 
          <div>
            <div className="bottom-buttons">
              <CopyButton selectedOffers={selectedOffers}/>
              <ShareDialog buttonText="deel lijst" infoText="Deel een link naar deze lijst met bewaarde aanbiedingen." />
            </div>
            <div>
              <header className="filter">
                <div className="filter-wrap">
                  <span className="bookmark-info">
                    Bewaarde aanbiedingen
                  </span>
                  {/* <span className="bookmark-old-info">{verlopenMelding(oldBookmarksExist)}</span> */}
                </div>
              </header>
              <Suspense fallback={<div className="even-geduld"><div className="notify-wrap"><span className='dot-dot-dot'></span></div></div>}>
                <ProductsContainer selectedOffers={selectedOffers}/>
              </Suspense>
            </div>
          </div> : <NoBookmarks />
        }
        
    </div>
  )
}

export default Bookmarks;
  