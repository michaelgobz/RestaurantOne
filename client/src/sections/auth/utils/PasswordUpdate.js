import { useState } from 'react';
import { useNavigate } from 'react-router';
// @mui
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox, Typography } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../../components/iconify';


// ----------------------------------------------------------------------

export default function UpdatePassword() {

    const UpdatePassword = '/auth/login'

    const url = `${process.env.REACT_APP_API}${UpdatePassword}`;
    console.log(url)
    const navigator = useNavigate()

    // get data from the form
    const [password, setPassword] = useState('');
    const [retypePassword, setRetypePassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [data, setData] = useState({
        password: '',
        retypedPassword: '',
    });

    const HandleSetEmail = (e) => {
        setEmail(e.target.email)
    }

    const HandleSetPassword = (e) => {
        setPassword(e.target.password)
    }
    const requestOptions = {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' },
    };

    const HandleUpdatePassword = () => {
        console.log(data)
        if (sessionStorage.getItem('auth') !== 'true') {
            console.log('clicked');
            fetch(url, requestOptions)
                .then((response) => {
                    if (response.status === 200) {
                        const session = response.json()
                        console.log(session)
                        sessionStorage.setItem(session.key, session.value)
                        sessionStorage.setItem('auth', 'true')
                        navigator('/auth/login')
                    } else {
                        console.log('some error has happened')
                    }
                }).catch((reason) => {
                    console.log(`This {reason} issue has happened`)
                })
        } else {
            navigator('/auth/login')
        }
    };

    const HandleChange = (e) => {
        setData({ ...data, [e.target.name]: e.target.value });
    };

    return (
        <>
            <Stack spacing={3}>

                <TextField
                    name="New password"
                    label="New Password"
                    value={newPassword}
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
                    value={newPassword}
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


            <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={HandleUpdatePassword}>
                Update Password
            </LoadingButton>
        </>
    );
}
