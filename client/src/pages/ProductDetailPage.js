import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import {LoadingSpinner} from '../sections/loadingspinner';
import ProductDetails from '../sections/products/ProductDetails';


const ProductDetailContainer = () => {
    const [item, setItem] = useState(null);
    const { itemId } = useParams();



    const url = `${process.env.REACT_APP_API}/dashboard/menu_item/${itemId}`;

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
                setItem(data.elements);
            }).catch((error) => {
                console.log(error);
            });
    }, [url]);


    return (
        item ? <ProductDetails Product={item} />
            : <LoadingSpinner text='loading product ...' />);

};

export default ProductDetailContainer;