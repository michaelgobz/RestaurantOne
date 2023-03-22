import { Helmet } from 'react-helmet-async';


// @mui
import { styled } from '@mui/material/styles';
import { Container, Typography, Divider, Stack, Button } from '@mui/material';
// hooks
import useResponsive from '../hooks/useResponsive';

// components

import UpdatePassword from '../sections/auth/utils/PasswordUpdate';


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

export default function UpdatePasswordPage() {

    const mdUp = useResponsive('up', 'md')

    return (
        <>
            <Helmet>
                <title> New Password | Open Restaurant </title>
            </Helmet>

            <StyledRoot>

                <Container maxWidth="sm">
                    <StyledContent>
                        <Typography variant="h4" gutterBottom>
                            Create new password
                        </Typography>

                        <Typography variant="body2" sx={{ mb: 5 }}>
                            Please enter your new password
                        </Typography>

                        <Divider sx={{ my: 3 }} />

                        <UpdatePassword />
                    </StyledContent>
                </Container>
            </StyledRoot>
        </>
    );
}
