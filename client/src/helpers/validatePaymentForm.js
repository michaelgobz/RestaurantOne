export default function validatePaymentForm(values, setError) {
  const errors = {};

  // cardNumber

  if (!values.cardNumber) {
    errors.cardNumber = 'Numbers is required';
  } else if (values.cardNumber?.length < 16 || values.cardNumber?.length > 16) {
    errors.cardNumber = 'Numbers must be 16 characters';
  } else if (!/^[0-9]*$/i.test(values.cardNumber)) {
    errors.cardNumber = 'Numbers should be numeric';
  }

  // cardName

  if (!values.cardName) {
    errors.cardName = 'Card Name is required';
  } else if (values.cardName?.length < 3) {
    errors.cardName = 'Card Name must be at least 3 characters';
  } else if (!/^[A-Za-z]+(?:[ _-][A-Za-z]+)*$/i.test(values.cardName)) {
    errors.cardName = 'Card Name should be Alphabetic';
  }

  // cardExpDate

  if (!values.cardExpDate) {
    errors.cardExpDate = 'Expiration Date is required';
  }

  // cardCvv

  if (!values.cardCvv) {
    errors.cardCvv = 'Pin is required';
  } else if (values.cardCvv?.length !== 3) {
    errors.cardCvv = 'Pin must be 3 characters';
  } else if (!/^[0-9]*$/i.test(values.cardCvv)) {
    errors.cardCvv = 'Pin should be numeric';
  }

  setError(errors);

  return Object.keys(errors).length === 0;
}
