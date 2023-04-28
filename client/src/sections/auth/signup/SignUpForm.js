import { useState } from 'react';
import { useNavigate } from 'react-router'
// @mui
import { Stack, IconButton, InputAdornment, TextField, Checkbox, Typography } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../../components/iconify';

// ----------------------------------------------------------------------

export default function SignUpForm() {
  const url = `${process.env.REACT_APP_API}/auth/signup`;
  console.log(url)

  const navigator = useNavigate()
  const [showPassword, setShowPassword] = useState(false);

  const [data, setData] = useState({
    firstname: '', lastname: '', email: '', password: '', retypePassword: '',
    phoneNumber: ''
  })

  const HandleChange = (e) => {
    setData({ ...data, [e.target.name]: e.target.value })
  }

  const requestOptions = {
    method: 'POST',
    mode: 'cors',
    body: JSON.stringify(data),
    headers: { 'Content-Type': 'application/json' },
  };

  const HandleSignUp = () => {
    fetch(url, requestOptions).then
      (response => {
        response.json().then((data) => {
          console.log(data)
          if (response.status === 200) {
            console.log(data.token)
            // we need to get varification token form the response
            sessionStorage.setItem('verification_token', data.token)
            navigator('/auth/confirm-account')
            // need to verify the user
          } else {
            console.log('some error has happened')
          }

      }).catch((reason) => {
        console.log(`This ${reason} happened and caused the error in the fetch request`)
      }).finally(() => {
        console.log()
      })
      })
  };

  return (
    <>
      <Stack spacing={3}>
        <TextField name="firstname" onChange={HandleChange} label="First Name" />
        <TextField name="lastname" onChange={HandleChange} label="Last Name" />
        <TextField name="email" onChange={HandleChange} label="Email address" />
        <TextField
          name="password"
          label="Password"
          onChange={HandleChange}
          type={showPassword ? 'text' : 'password'}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton onClick={() => setShowPassword(!showPassword)} edge="end">
                  <Iconify icon={showPassword ? 'eva:eye-fill' : 'eva:eye-off-fill'} />
                </IconButton>
              </InputAdornment>
            ),
          }}
        />
        <TextField
          name="Retype-password"
          label="Retype Password"
          onChange={HandleChange}
          type={showPassword ? 'text' : 'password'}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton onClick={() => setShowPassword(!showPassword)} edge="end">
                  <Iconify icon={showPassword ? 'eva:eye-fill' : 'eva:eye-off-fill'} />
                </IconButton>
              </InputAdornment>
            ),
          }}
        />
        <TextField onChange={HandleChange} name="Phonenumber" label="Phone number" />

      </Stack>

      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ my: 2 }}>
        <Checkbox name="remember" label="Remember me" />
        <Typography> Accept the privacy policy and T&Cs</Typography>
      </Stack>

      <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={HandleSignUp}>
        Sign Up
      </LoadingButton>
    </>
  );
};