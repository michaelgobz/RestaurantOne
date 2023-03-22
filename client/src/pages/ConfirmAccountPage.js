import { Helmet } from 'react-helmet-async';


// @mui
import { styled } from '@mui/material/styles';
import { Container, Typography, Divider, Stack, Button } from '@mui/material';
// hooks
import useResponsive from '../hooks/useResponsive';

// components

import ConfirmAccount from '../sections/auth/utils/ConfirmAccount';


// ----------------------------------------------------------------------

const StyledRoot = styled('div')(({ theme }) => ({
    [theme.breakpoints.up('md')]: {
        display: 'flex',
    },
}));

const StyledSection = styled('div')(({ theme }) => ({
    width: '100%',
    maxWidth: 480,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    boxShadow: theme.customShadows.card,
    backgroundColor: theme.palette.background.default,
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

export default function ConfirmAccountPage() {

    const mdUp = useResponsive('up', 'md')

    return (
        <>
            <Helmet>
                <title> ConfirmAccount | Open Restaurant </title>
            </Helmet>

            <StyledRoot>

                <Container maxWidth="sm">
                    <StyledContent>
                        <Typography variant="h4" gutterBottom>
                            Confirm Account
                        </Typography>

                        <Typography variant="body2" sx={{ mb: 5 }}>
                            Enter the token you received in your email to verify account
                        </Typography>

                        <Divider sx={{ my: 3 }} />

                        <ConfirmAccount />
                    </StyledContent>
                </Container>
            </StyledRoot>
        </>
    );
}
