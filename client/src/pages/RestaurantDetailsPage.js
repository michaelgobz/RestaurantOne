import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import RestaurantDetails from '../sections/reservation/RestaurantDetails';
import LoadingSpinner from '../sections/LoadingSpinner';



const RestaurantDetailContainer = () => {
    const [item, setItem] = useState(null);
    const { restaurantId } = useParams();



    const url = `${process.env.REACT_APP_API}/dashboard/restaurants/${restaurantId}`;

    // fetch the data
    useEffect(() => {
        const requestOptions = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        };

        fetch(url, requestOptions).then((response) => response.json())

            .then((data) => {
                setItem(data.restaurant);
            }).catch((error) => {
                console.log(error);
            });
    }, [url]);


    return (
        // needs to be changed to restaurant details
        item ? <RestaurantDetails Restaurant={item} />
            : <LoadingSpinner />);

};

export default RestaurantDetailContainer;