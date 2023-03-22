import { useState } from 'react';
import { useNavigate } from 'react-router';
// @mui
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox, Typography } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../../components/iconify';


// ----------------------------------------------------------------------

export default function LoginForm() {

  const recoverPassword = `${process.env.REACT_APP_CLIENT}/auth/forgot-password`;

  const login = '/auth/login'

  const url = `${process.env.REACT_APP_API}${login}`;
    console.log(url)
  const navigator = useNavigate()

  // get data from the form
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [data, setData] = useState({
    email: '',
    password: '',
  });

  const HandleSetEmail = (e) => {
      setEmail(e.target.email)
  }

  const HandleSetPassword = (e) => {
      setPassword(e.target.password)
  }
  const form = {
      email,
      password
  }
  const requestOptions = {
    method: 'POST',
    mode: 'cors',
    body: JSON.stringify(data),
    headers: { 'Content-Type': 'application/json' },
  };

  const HandleSubmit = () => {
      console.log(data)
      if(sessionStorage.getItem('auth') !== 'true'){
          console.log('clicked');
          fetch(url, requestOptions)
              .then((response) => {
                  if (response.status === 200) {
                      const session = response.json()
                      console.log(session)
                      sessionStorage.setItem(session.key, session.value)
                      sessionStorage.setItem('auth', 'true')
                      navigator('/customer/products')
          } else {
                      console.log('some error has happened')
          }
          }).catch((reason) => {
          console.log(`This {reason} issue has happened`)
          })
      } else  {
          navigator('/customer/products')
      }
  };

  const HandleChange = (e) => {
    setData({ ...data, [e.target.name]: e.target.value });
  };

  return (
    <>
      <Stack spacing={3}>
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
      </Stack>

      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ my: 2 }}>
        <Checkbox name="remember" label="Remember me" />
        <Typography variant='body5' sx={{ ml: -5 }}>Remember Me</Typography>
        <Link href={sessionStorage.getItem('signup') === 'true'? recoverPassword :null}variant="subtitle2" underline="hover">
          Forgot password?
        </Link>
      </Stack>

      <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={HandleSubmit}>
        Login
      </LoadingButton>
    </>
  );
}
