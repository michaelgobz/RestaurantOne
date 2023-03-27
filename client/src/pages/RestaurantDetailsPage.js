import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import RestaurantDetails from '../sections/reservation/RestaurantDetails';
import LoadingSpinner from '../sections/loadingSpinner/LoadingSpinner';



const RestaurantDetailContainer = () => {
    const [item, setItem] = useState(null);
    const { itemId } = useParams();
    const [loading, setLoading] = useState(true);

    const requestOptions = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const url = `${process.env.REACT_APP_API}/restaurants/${itemId}`;

    return (
        // needs to be changed to restaurant details
        item ? <RestaurantDetails />
            : <LoadingSpinner />);

};

export default RestaurantDetailContainer;