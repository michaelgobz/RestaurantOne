import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import RestaurantDetails from '../sections/reservation/RestaurantDetails';
import LoadingSpinner from '../sections/loadingSpinner/LoadingSpinner';



const RestaurantDetailContainer = () => {
    const [item, setItem] = useState(null);
    const { restaurantId } = useParams();
    const [loading, setLoading] = useState(true);

    const requestOptions = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const url = `${process.env.REACT_APP_API}/dashboard/restaurants/${restaurantId}`;

    // fetch the data
    useEffect(() => {
        fetch(url, requestOptions).then((response) => response.json())

            .then((data) => {
                setItem(data.restaurant);
            }).catch((error) => {
                console.log(error);
            });
    }, []);


    return (
        // needs to be changed to restaurant details
        item ? <RestaurantDetails Restaurant={item} />
            : <LoadingSpinner />);

};

export default RestaurantDetailContainer;