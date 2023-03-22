import { useState } from 'react';
import { useNavigate } from 'react-router'
// @mui
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox, Typography } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../../components/iconify';

// ----------------------------------------------------------------------

export default function SignUpForm() {
  const url = `${process.env.REACT_APP_API}/auth/signup`;
  console.log(url)

  const navigator = useNavigate()
  const [showPassword, setShowPassword] = useState(false);
  const [firstname, setFirstname] = useState('')
  const [lastname, setLastname] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [retypePassword, setRetypePassword] = useState('')
  const [phoneNumber, setPhoneNumber] = useState('')

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
        if (response.status === 200) {
          const session = response.json()
          console.log(session)
          // we need to get varification token form the response

          // need to verify the user
          navigator('/auth/login')
        } else {
          console.log('some error has happened')
        }
      })
  };

  return (
    <>
      <Stack spacing={3}>
        <TextField name="firstname" value={firstname} onChangeCapture={HandleChange} label="First Name" />
        <TextField name="lastname" value={lastname} onChangCapture={HandleChange} label="Last Name" />
        <TextField name="email" value={email} onChangeCapture={HandleChange} label="Email address" />
        <TextField
          name="password"
          label="Password"
          value={password}
          onChangeCapture={HandleChange}
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
          value={retypePassword}
          onChangeCapture={HandleChange}
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
        <TextField value={phoneNumber} onChangeCapture={HandleChange} name="Phonenumber" label="Phone number" />

      </Stack>

      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ my: 2 }}>
        <Checkbox name="remember" label="Remember me" />
        <Typography> Accept the privacy policy and T&Cs</Typography>
        <Link variant="subtitle2" underline="hover">
          Forgot password?
        </Link>
      </Stack>

      <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={HandleSignUp}>
        Sign Up
      </LoadingButton>
    </>
  );
};