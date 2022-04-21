import { Link } from "react-router-dom";
import localForage from 'localforage'
import React, {useState, useEffect } from "react";

function BookmarkButton(props) {

    const [bookmarkCount, setBookmarkCount] = useState(props.bookmarkCount);  

    const amountOfBookmarks = () => {
        localForage.getItem('teerkost-bookmarks').then(function (value) {
            var amount = 0
            if(value !== null) {
                amount = value.length
            }
            setBookmarkCount(amount)
        })
    } 
    
    useEffect(() => {
        amountOfBookmarks()
    },[])

    return (
        <div className="button-cell">
        <Link to="/bewaard"><div className="button personal-list-button">
            <i class="ri-bookmark-fill"></i> 
            <div className="personal-list-button-tag">{bookmarkCount}</div>
        </div></Link>
        </div>
    )
  }
  
  export default BookmarkButton;
    