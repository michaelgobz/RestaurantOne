import { useState } from 'react';
import { useNavigate } from 'react-router';
// @mui
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox, Typography } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../../components/iconify';


// ----------------------------------------------------------------------

export default function ConfirmAccount() {

    const confirm = '/auth/confirm-account'

    const url = `${process.env.REACT_APP_API}${confirm}`;
    console.log(url)
    const navigator = useNavigate()

    // get data from the form
    const [token, setToken] = useState('');
    const [data, setData] = useState({
        email: '',
        password: '',
    });

    const requestOptions = {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' },
    };

    const HandleConfirmAccount = () => {
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
                        navigator('/customer/products')
                    } else {
                        console.log('some error has happened')
                    }
                }).catch((reason) => {
                    console.log(`This {reason} issue has happened`)
                })
        } else {
            navigator('/customer/products')
        }
    };

    const HandleChange = (e) => {
        setData({ ...data, [e.target.name]: e.target.value });
    };

    return (
        <>
            <Stack spacing={3}>
                <TextField name="Token" value={token} onChangeCapture={HandleChange} label="Email address" />

            </Stack>

            <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={HandleConfirmAccount}>
                Confirm Account
            </LoadingButton>
        </>
    );
}
