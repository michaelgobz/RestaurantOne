import { useState } from 'react';
import { useNavigate } from 'react-router';
// @mui
import { Stack, TextField } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components


// ----------------------------------------------------------------------

export default function ForgotPassword() {

    const forgot = '/auth/forgot-password'

    const url = `${process.env.REACT_APP_API}${forgot}`;
    console.log(url)
    const navigator = useNavigate()

    // get data from the form
    const [email] = useState('');
    const [data, setData] = useState({
        email: ''
    });

    const requestOptions = {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' },
    };

    const HandleVerifyEmail = () => {
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
                        navigator('/auth/update-password')
                    } else {
                        console.log('some error has happened')
                    }
                }).catch((reason) => {
                    console.log(`This ${reason} happened and caused the error in the fetch request`)
                })
        } else {
            navigator('/auth/update-password')
        }
    };

    const HandleChange = (e) => {
        setData({ ...data, [e.target.name]: e.target.value });
    };

    return (
        <>
            <Stack spacing={3}>
                <TextField fullWidth label="Email" name="email" onChange={HandleChange} type="email" value={email}
                    sx={{ my: 3 }}
                    variant="outlined" />
            </Stack>
            <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={HandleVerifyEmail}>
                Confirm Email Address
            </LoadingButton>
        </>
    );
}
