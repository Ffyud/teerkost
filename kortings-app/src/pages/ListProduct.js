import React, {useState, useEffect, Suspense} from "react";
import { useParams } from "react-router-dom";
import Offers from '../offers.json';
import ShareDialog from "../components/ShareDialog";
import BookmarkButton from "../BookmarkButton";
import { categoryList } from "../Categories";

const ProductsContainer = React.lazy(() => import ('../ProductsContainer'));

function Main(props) {
  
  var { id } = useParams();

  const createProductIdsList = (id) => {
    var productIdFilter = object => object.productId === null;

    const ids = id.split(',')
    console.log(ids)
    const aantal = ids.length
    console.log(aantal)

    productIdFilter = object => ids.includes(object.productId);
    var filtered = Offers.filter(productIdFilter)
    setSelectedOffers(filtered);
  }

  useEffect(() => {
    window.scrollTo(0, 0);
  });

  const [selectedOffers, setSelectedOffers] = useState(Offers);
  const [productIdsList, setProductIdsList] = useState([]);  

  useEffect(() => {
    createProductIdsList(id)
  }, [])

  return (
    <div className="app-wrap">
        <div className="bottom-buttons">
          <BookmarkButton />
          <ShareDialog buttonText="deel pagina" infoText="Deel de huidige pagina met de gekozen filters." />
        </div>
        <a className="title-sober" href='https://teerkost.nl'><span>Teerkost</span></a>
        <header className="filter">
            <div id="filter-dialog">
            <div className="filter-wrap">

            </div>
            </div>
        </header>
        <Suspense fallback={<div className="even-geduld"><div className="notify-wrap"><span className='dot-dot-dot'></span></div></div>}>
            <ProductsContainer selectedOffers={selectedOffers}/>
        </Suspense>
    </div>
  )
}

export default Main;
  