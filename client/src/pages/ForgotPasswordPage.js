import { Helmet } from 'react-helmet-async';


// @mui
import { styled } from '@mui/material/styles';
import { Container, Typography, Divider } from '@mui/material';
// hooks
import useResponsive from '../hooks/useResponsive';

// components

import ForgotPassword from '../sections/auth/utils/ForgotPassword';


// ----------------------------------------------------------------------

const StyledRoot = styled('div')(({ theme }) => ({
    [theme.breakpoints.up('md')]: {
        display: 'flex',
    },
}));

const StyledContent = styled('div')(({ theme }) => ({
    maxWidth: 480,
    margin: 'auto',
    minHeight: '100vh',
    display: 'flex',
    justifyContent: 'center',
    flexDirection: 'column',
    padding: theme.spacing(12, 0),
}));


// ----------------------------------------------------------------------

export default function ForgotPasswordPage() {


    return (
        <>
            <Helmet>
                <title> ForgotPassword | Open Restaurant </title>
            </Helmet>

            <StyledRoot>

                <Container maxWidth="sm">
                    <StyledContent>
                        <Typography variant="h4" gutterBottom align='center'>
                            Recover Password
                        </Typography>

                        <Typography variant="body5" sx={{ my: 5 }} align='center'>
                            Please enter your email address below and we will send you instructions on how to reset your password.
                        </Typography>

                        <Divider sx={{ my: 3 }} />

                        <ForgotPassword />
                    </StyledContent>
                </Container>
            </StyledRoot>
        </>
    );
}
