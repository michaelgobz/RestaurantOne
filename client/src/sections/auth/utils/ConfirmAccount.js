import { useState } from 'react';
import { useNavigate } from 'react-router';
// @mui
import { Stack, TextField } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components


// ----------------------------------------------------------------------

export default function ConfirmAccount() {

    const confirm = '/auth/confirm_account'

    const url = `${process.env.REACT_APP_API}${confirm}/${sessionStorage.getItem('verification_token')}`;
    console.log(url)
    const navigator = useNavigate()
    const [token] = useState('');

    // get data from the form
    const [data, setData] = useState({
        token: ''
    });

    const requestOptions = {
        method: 'GET',
        mode: 'cors',
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
                        navigator('/auth/login')
                    } else {
                        console.log('some error has happened')
                    }
                }).catch((reason) => {
                    console.log(`This ${reason} happened and caused the error in the fetch request`)
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
                <TextField name="Token" value={token} onChange={HandleChange} label="Token" sx={{ my: 5 }} />

            </Stack>

            <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={HandleConfirmAccount}>
                Confirm Account
            </LoadingButton>
        </>
    );
}
