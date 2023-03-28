import { useState } from 'react';
import { useNavigate } from 'react-router';
// @mui
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox, Typography } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../../components/iconify';


// ----------------------------------------------------------------------

export default function UpdatePassword() {

    // get hold of the use's email and if it is valid

    const UpdatePassword = '/auth/update-password'

    const url = `${process.env.REACT_APP_API}${UpdatePassword}`;
    console.log(url)
    const navigator = useNavigate()

    // get data from the form
    const [newPassword, setNewPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [data, setData] = useState({
        password: '',
        confirmedPassword: '',
    });

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
                    console.log(`This ${reason} happened and caused the error in the fetch request`)
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
                    name="Confirm password"
                    label="Confirm  Password"
                    value={confirmPassword}
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
                    sx={{ my: 5 }}
                />
            </Stack>


            <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={HandleUpdatePassword}
                sx={{ my: 5 }}>
                Update Password
            </LoadingButton>
        </>
    );
}
