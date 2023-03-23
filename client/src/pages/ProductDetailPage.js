import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import LoadingSpinner from '../sections/loadingSpinner/LoadingSpinner';
import ProductDetails from '../sections/products/ProductDetails';


const ProductDetailContainer = () => {
    const [item, setItem] = useState(null);
    const { itemId } = useParams();
    const [loading, setLoading] = useState(true);

    const requestOptions = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const url = `${process.env.REACT_APP_API}/products/${itemId}`;

    useEffect(async () => {
        // get the product from the db
        const response = await fetch(url, requestOptions);
        const data = await response.json();
        setItem(data);
    }, [itemId]);

    return (
        item ? <ProductDetails {...item} />
            : <LoadingSpinner />);

};

export default ProductDetailContainer;