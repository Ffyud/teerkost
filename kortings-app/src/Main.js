import React, {useState, useEffect, Suspense} from "react";
import Offers from './offers.json';

const ProductsContainer = React.lazy(() => import ('./ProductsContainer'));

function Main(props) {
  
  let categories = [
    ['bier', 0], ['koffie', 0], ['groente', 0], ['vis', 0],['fruit', 0],['kant-en-klaar', 0],
    ['wijn', 0], ['aardappel', 0], ['brood', 0], ['kaas', 0], ['noten', 0], ['zuivel', 0], 
    ['vlees', 0], ['frisdrank', 0], ['verzorging', 0], ['huishouden', 0]
  ]

  const [categoriesList, setCategoriesList] = useState(categories)

  useEffect(() => {
    window.scrollTo(0, 0);
    window.addEventListener("scroll", handleScroll);
  });

  const handleScroll = () => {
    const position = window.pageYOffset;
    var dealFilter = document.querySelector("div.filter-deal")
    if(dealFilter.querySelector('#active-deal') === null)
    {
      if(position > 200) {
        dealFilter.classList.add("filter-move-away")
      }
      else {
        dealFilter.classList.remove("filter-move-away")
      }
    }
  }

  const [selectedOffers, setSelectedOffers] = useState(Offers);  
  const [selectedShopRoute, setSelectedShopRoute] = useState(props.shop);
  const [selectedDealRoute, setSelectedDealRoute] = useState(props.deal);
  const [selectedCatRoute, setSelectedCatRoute] = useState(props.cat);

  useEffect(() => {
    toggleFilterButton(selectedShopRoute, "shop")
    toggleFilterButton(selectedCatRoute, "category")
    toggleFilterButton(selectedDealRoute, "deal")

    setCounterPerCategory(selectedShopRoute)

    updateOfferList(selectedShopRoute, selectedCatRoute, selectedDealRoute)
  }, [])

  const setCounterPerCategory = (shop) => {
    if(shop !== undefined) {
      var shopFilter = object => object.shop === shop;

    }
    else {
      var shopFilter = object => object.shop !== null;
    }
  
    let tempList = []
    categoriesList.map((category, key) => {
      var categoryFilter = object => object.category === category[0];

      var filterByCategory = Offers.filter(shopFilter).filter(categoryFilter)
      var numberCountByCategory = filterByCategory.length

      let categoryObjectTemp = [category[0], numberCountByCategory]
      return tempList.push(categoryObjectTemp)
    })
    setCategoriesList(tempList)
  }

  const clickOnShop = (name) => {
    toggleFilterButton(name, "shop")
    if(selectedShopRoute === name) {
      name = undefined
    }
    setSelectedShopRoute(name)
    setCounterPerCategory(name)
    updateOfferList(name, selectedCatRoute, selectedDealRoute)
  }

  const clickOnCat = (name) => {
    toggleFilterButton(name, "category")
    if(selectedCatRoute === name) {
      name = undefined
    }
    setSelectedCatRoute(name)
    updateOfferList(selectedShopRoute, name, selectedDealRoute)
  }

  const clickOnDeal = (name) => {
    toggleFilterButton(name, "deal")
    if(selectedDealRoute === name) {
      name = undefined
    }
    setSelectedDealRoute(name)
    updateOfferList(selectedShopRoute, selectedCatRoute, name)
  }

  const toggleFilterButton = (name, type) => {
      var htmlIdActive = "active-" + type
      var element = document.querySelectorAll(`[data-${type}="${name}"]`)
      var node = element.item(0)
      if(node != null) {
        if(node.hasAttribute("id")) {
          node.removeAttribute("id") // deactivate the clicked element
        }
        else {
          var activeElement = document.getElementById(htmlIdActive)
          if(activeElement != null) { activeElement.removeAttribute("id")} // deactivate any other element
          
          node.id = htmlIdActive // activate the clicked element
        }
      }
  }

  const updateOfferList = (selectedShopRoute, selectedCatRoute, selectedDealRoute) => {
    var shopFilter = object => object.shop !== null;
    var dealFilter = object => object.deal !== null;
    var categoryFilter = object => object.category !== null;

    if(selectedCatRoute !== undefined) {
      categoryFilter = object => object.category === selectedCatRoute;
      console.log("Filter voor category met " + selectedCatRoute + " ingesteld.")
    }

    if(selectedDealRoute !== undefined) {
      dealFilter = object => object.deal === selectedDealRoute;
      console.log("Filter voor deal met " + selectedDealRoute + " ingesteld.")
    }

    if(selectedShopRoute !== undefined) {
      shopFilter = object => object.shop === selectedShopRoute;
      console.log("Filter voor shop met " + selectedShopRoute + " ingesteld.")
    }
    console.log("Totale aantal aanbiedingen: " + Offers.length)

    var filtered = Offers.filter(shopFilter).filter(dealFilter).filter(categoryFilter)
    
    setSelectedOffers(filtered);
    console.log("Aantal aanbiedingen na filter: " + filtered.length)
  }

  const shareApi = () => {
    if (navigator.share) {
      navigator.share({
        title: 'Teerkost',
        url: 'https://teerkost.nl'
      }).then(() => {
        console.log('Dankje');
      })
      .catch(console.error);
    } else {
      // shareDialog.classList.add('is-open');
      console.log("helaas dit werkt niet")
    }
  }
  
  return (
    <div>
        <header className="filter">
            {navigator.share && (
                <div onClick={shareApi} className="share-button">
                  <i class="ri-share-box-fill"></i>
                </div>
            )}  
            <div id="filter-dialog">
            <div className="filter-wrap">
                <div className="filter-shop">
                  <span onClick={() => clickOnShop("ah")} data-shop="ah">Albert Heijn</span>
                  <span onClick={() => clickOnShop("jumbo")}  data-shop="jumbo">Jumbo</span>
                  <span onClick={() => clickOnShop("lidl")} data-shop="lidl">Lidl</span>
                  <span onClick={() => clickOnShop("aldi")}  data-shop="aldi">Aldi</span>
                </div>
                <div className="filter-cat">
                  {categoriesList.map((category, key) => {
                    if(category[1] === 0) {
                      return <span className='filter-no-interest' key={key} onClick={() => clickOnCat(category[0])} data-category={category[0]}>{category[0]}</span>
                    }
                    else {
                      return <span key={key} onClick={() => clickOnCat(category[0])} data-category={category[0]}>{category[0]} <i className="counter" data-category="bier">{category[1]}</i></span>
                    }
                  })}
                </div>
                <div className="filter-deal">
                  <span onClick={() => clickOnDeal("1+1 gratis")} data-deal="1+1 gratis">1+1</span>
                  <span onClick={() => clickOnDeal("2+1 gratis")} data-deal="2+1 gratis">2+1</span>
                  <span onClick={() => clickOnDeal("3+1 gratis")} data-deal="3+1 gratis">3+1</span>
                  <span onClick={() => clickOnDeal("10% korting")} data-deal="10% korting">10%</span>
                  <span onClick={() => clickOnDeal("25% korting")} data-deal="25% korting">25%</span>
                  <span onClick={() => clickOnDeal("30% korting")} data-deal="30% korting">30%</span>
                  <span onClick={() => clickOnDeal("40% korting")} data-deal="40% korting">40%</span>
                  <span onClick={() => clickOnDeal("50% korting")} data-deal="50% korting">50%</span>
                  <span onClick={() => clickOnDeal("2e halve prijs")} data-deal="2e halve prijs">2e halve prijs</span>
                  <span onClick={() => clickOnDeal("op=op")} data-deal="op=op">op=op</span>
                </div>
            </div>
            </div>
        </header>
        <Suspense fallback={<div className="even-geduld">Even geduld...</div>}>
            <ProductsContainer selectedOffers={selectedOffers}/>
        </Suspense>
    </div>
  )
}

export default Main;
  