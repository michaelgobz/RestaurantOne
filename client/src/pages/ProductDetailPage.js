import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import LoadingSpinner from '../sections/loadingSpinner/LoadingSpinner';
import ProductDetails from '../sections/products/ProductDetails';


const ProductDetailContainer = () => {
    const [item, setItem] = useState(null);
    const { itemId } = useParams();

    const requestOptions = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const url = `${process.env.REACT_APP_API}/dashboard/menu_item/${itemId}`;

    // fetch the data
    useEffect(() => {
        fetch(url, requestOptions).then((response) => response.json())
            .then((data) => {
                setItem(data.elements);
            }).catch((error) => {
                console.log(error);
            });
    }, [api, requestOptions]);


    return (
        item ? <ProductDetails Product={item} />
            : <LoadingSpinner />);

};

export default ProductDetailContainer;