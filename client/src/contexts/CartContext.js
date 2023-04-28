import { useState, createContext } from 'react';
import PropTypes from 'prop-types';

export const CartContext = createContext();



export const CartProvider = ({ children }) => {

  const [cart, setCart] = useState(
    JSON.parse(localStorage.getItem('cart')) || []
  );

  // cart methods

  const addItemToCart = (item) => {
    setCart([...cart, item]);
    localStorage.setItem('cart', JSON.stringify([...cart, item]));
  };

  const removeItemFromCart = (id) => {
    setCart(cart.filter((cartItem) => cartItem.id !== id));
    localStorage.setItem(
      'cart',
      JSON.stringify(cart.filter((cartItem) => cartItem.id !== id))
    );
  };

  const isInCart = (itemId) => cart.some((cartItem) => cartItem.id === itemId);

  const amountOfItemsInCart = () =>
      // eslint-disable-next-line no-return-assign
    cart.reduce((acc, item) => (acc += item.quantity), 0);
  /**
   * function totalCartPrice() {
      return cart.reduce((acc, item) => (acc += item.price * item.quantity), 0);
    }
  
   * 
   */


  const resetCart = () => {
    setCart([]);
    localStorage.setItem('cart', JSON.stringify([]));
  };

  return (
    <>
      <CartContext.Provider
        value={{
          cart,
          setCart,
          addItemToCart,
          removeItemFromCart,
          isInCart,
          amountOfItemsInCart,
          // totalCartPrice,
          resetCart,
        }}
      >
        {children}
      </CartContext.Provider>
    </>

  );
};

CartProvider.propTypes = {
  children: PropTypes.node.isRequired,
};
