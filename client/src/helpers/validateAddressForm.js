export default function validateAddressForm(values, setErrors) {
  const errors = {};

  // name

  if (!values.name) {
    errors.name = 'Name is required;
  } else if (values.name?.length < 3) {
    errors.name = 'Name must be at least 3 characters';
  } else if (!/^[A-Za-z]+(?:[ _-][A-Za-z]+)*$/i.test(values.name)) {
    errors.name = 'Name should be Alphabetic';
  }

  // lastName

  if (!values.lastName) {
    errors.lastName = 'Last Name is required';
  } else if (values.lastName?.length < 3) {
    errors.lastName = ' Last Name must be at least 3 characters';
  } else if (!/^[A-Za-z]+(?:[ _-][A-Za-z]+)*$/i.test(values.lastName)) {
    errors.lastName = 'Last Name should be Alphabetic';
  }

  // email

  if (!values.email) {
    errors.email = 'Email is required';
  } else if (values.email?.length < 3) {
    errors.email = 'Email must be at least 3 characters';
  } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)) {
    errors.email = 'Email should have a valid format with and @ and a dot';
  }

  //address

  if (!values.address) {
    errors.address = 'Address is required';
  } else if (values.address?.length < 10) {
    errors.address = 'Address must be at least 10 characters';
  }

  // city

  if (!values.city) {
    errors.city = 'City is required';
  } else if (values.city?.length < 3) {
    errors.city = 'City must be at least 3 characters';
  } else if (!/^[A-Za-z]+(?:[ _-][A-Za-z]+)*$/i.test(values.city)) {
    errors.city = 'City should be Alphabetic';
  }


  // country area

  if (!values.countryArea) {
    errors.countryArea = 'Country Area is required';
  } else if (values.state?.length < 3) {
    errors.state = 'Country Area must be at least 3 characters';
  } else if (!/^[A-Za-z]+(?:[ _-][A-Za-z]+)*$/i.test(values.state)) {
    errors.state = 'Country Area should be Alphabetic';
  }

  // city area

  if (!values.cityArea) {
    errors.cityArea = 'City Area is required';
  } else if (values.cityArea?.length < 3) {
    errors.cityArea = 'City Area must be at least 3 characters';
  } else if (!/^[A-Za-z]+(?:[ _-][A-Za-z]+)*$/i.test(values.cityArea)) {
    errors.cityArea = 'City Area should be Alphabetic';
  }

  // notes

  if (!values.notes) {
    errors.notes = 'Notes is not required';
  } else if (values.zip?.length < 4 || values.zip?.length > 6) {
    errors.zip = "notes  must be between 10 and 200 characters"
  } else if (!/^[A-Za-z]+(?:[ _-][A-Za-z]+)*$/i.test(values.notes)) {
    errors.zip = 'notes should be Alphabetic';
  }

  // phoneNumber

  if (!values.phoneNumber) {
    errors.phoneNumber = 'Telephone Number is required';
  } else if (
    values.phoneNumber?.length < 8 ||
    values.phoneNumber?.length > 10
  ) {
    errors.phoneNumber = 'Telephone Number must be between 8 and 10 characters';
  } else if (!/^[0-9]{8,10}$/i.test(values.phoneNumber)) {
    errors.phoneNumber = 'Telephone Number should be Numeric';
  }

  setErrors(errors);

  return Object.keys(errors).length === 0;
}
