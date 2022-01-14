import React, {useState} from "react";
import './App.css';
import Offers from './offers.json';
import Product from './Product';

const expandFilter = () => {
  var dialog = document.getElementById("filter-dialog");
  dialog.classList.toggle('toggle-on');
}

function App() {

  const toggleFilterClass = (clickedElement, type) => {
    if(type === 'offer') {
      var otherElementOffer = document.getElementById('active-offer')
      if(otherElementOffer !== null) { 
        if(otherElementOffer === clickedElement) {
          clickedElement.removeAttribute("id")
        }
        else {
          otherElementOffer.removeAttribute("id") 
          clickedElement.id = 'active-offer'
        }
      }
      else {
        clickedElement.id = 'active-offer'
      }
    }
    else if(type === 'shop') {
      var otherElementShop = document.getElementById('active-shop')
      if(otherElementShop !== null) { 
        if(otherElementShop === clickedElement) {
          clickedElement.removeAttribute("id")
        }
        else {
          otherElementShop.removeAttribute("id") 
          clickedElement.id = 'active-shop'
        }
      }
      else {
        clickedElement.id = 'active-shop'
      }
    }
  }

  const setFilterByActiveElements = () => {
    var activeShop = document.getElementById("active-shop");
    var activeOffer = document.getElementById("active-offer");

    if(activeShop !== null && activeOffer === null) {
      var activeShopValue = activeShop.getAttribute('data-shop');
      var filtered = Offers.filter(object => object.shop === activeShopValue)
    }
    else if(activeShop === null && activeOffer !== null) {
      var activeOfferValue = activeOffer.getAttribute('data-offer');
      var filtered = Offers.filter(object => object.deal === activeOfferValue)
    }
    else if(activeShop !== null && activeOffer !== null){
      var activeShopValue = activeShop.getAttribute('data-shop');
      var activeOfferValue = activeOffer.getAttribute('data-offer');
      var filtered = Offers.filter(object => object.deal === activeOfferValue && object.shop === activeShopValue)
    }
    else {
      var filtered = Offers
    }

    setSelectedOffers(filtered);

    console.log("Shop filter '" + activeShopValue + "' gebruiken")
    console.log("Offer filter '" + activeOfferValue + "' gebruiken")

  }

  const filterOffer = (e) => {
    toggleFilterClass(e.target, "offer")
    setFilterByActiveElements()
  }

  const filterShop = (e) => {
    toggleFilterClass(e.target, "shop")
    setFilterByActiveElements()
  }

  const [selectedOffers, setSelectedOffers] = useState(Offers);  

  return (
    <div className="App">
      <div className="filter">
        <div id="filter-dialog">  
        <div className="filter-shop">
            <span onClick={filterShop} data-shop="AH">Albert Heijn</span>
            <span onClick={filterShop} data-shop="Jumbo">Jumbo</span>
          </div>
          <div className="filter-offer">
            <span onClick={filterOffer} data-offer="1+1 gratis">1+1 gratis</span>
            <span onClick={filterOffer} data-offer="2+1 gratis">2+1 gratis</span>
            <span onClick={filterOffer} data-offer="3+1 gratis">3+1 gratis</span>
            <span onClick={filterOffer} data-offer="10% korting">10% korting</span>
            <span onClick={filterOffer} data-offer="25% korting">25% korting</span>
            <span onClick={filterOffer} data-offer="30% korting">30% korting</span>
            <span onClick={filterOffer} data-offer="40% korting">40% korting</span>
            <span onClick={filterOffer} data-offer="50% korting">50% korting</span>
            <span onClick={filterOffer} data-offer="2e halve prijs">2e halve prijs</span>
          </div>
          {/* <div className="filter-cat">
            <span>🍺</span>
            <span>🍞</span>
            <span>🥫</span>
          </div> */}
        </div>
        <div className="filter-button" onClick={expandFilter}>FILTEREN</div>
      </div>
      {/* <div id="logo">KORTINGS</div> */}
      <div className="flex-container">
      {selectedOffers.map(function(name, index){
        return <Product key={index} item={name}/>;
      })}
      </div>
    </div>
  );
}

export default App;
