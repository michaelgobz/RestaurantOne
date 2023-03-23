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

    return (
        item ? <ProductDetails />
            : <ProductDetails />);

};

export default ProductDetailContainer;