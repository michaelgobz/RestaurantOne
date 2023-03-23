import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import LoadingSpinner from '../sections/loadingSpinner/LoadingSpinner';
import RestaurantDetails from 'src/sections/reservation/RestaurantDetails';


const RestaurantDetailContainer = () => {
    const [item, setItem] = useState(null);
    const { itemId } = useParams();
    const [loading, setLoading] = useState(true);
    const request_options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const url = `${process.env.REACT_APP_API}/restaurants/${itemId}`;

    useEffect(async () => {
        // get the product from the db
        const response = await fetch(url, request_options);
        const data = await response.json();
        setItem(data);
    }, [itemId]);

    return (
        // needs to be changed to restaurant details
        item ? <RestaurantDetails />
            : <LoadingSpinner />);

};

export default RestaurantDetailContainer;