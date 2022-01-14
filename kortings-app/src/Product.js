function Product(props) {
  if(props.item['shop'] === 'AH') {
    return (
      <div className="flex-item shop-ah">
        <span className="product-image"><img alt={props.item['product']} src={props.item['image']}/></span>
        <span className="product-name">
          {props.item['product']}
          <span className="product-info"> {props.item['productInfo']}</span>
        </span>
        <span className='product-date-end'>{props.item['dateEnd']}</span>
        <span className="product-price">{props.item['price']}</span>   
        <span className="product-deal">{props.item['deal']}</span>
   
      </div>
    )
  }
  else
    return (
      <div className="flex-item shop-jumbo">
        <span className="product-image"><img alt={props.item['product']} src={props.item['image']}/></span>
        <span className="product-name">
          {props.item['product']}
          <span className="product-info"> {props.item['productInfo']}</span>
        </span>
        <span className='product-date-end'>{props.item['dateEnd']}</span>
        <span className="product-price">{props.item['price']}</span> 
        <span className="product-deal">{props.item['deal']}</span>
     
      </div>
    )


// {
//   "product": "Campina en Valess - bij 12 euro gratis bezorging",
//   "productInfo": "hele week",
//   "deal": "gratis bezorging bij 12 euro",
//   "price": 0,
//   "dateStart": "2022-01-10",
//   "dateEnd": "2022-01-16",
//   "link": "https://ah.nl/bonus/groep/FREE0222_E?week=2",
//   "shop": "AH"
// }
}

export default Product;
