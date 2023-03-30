import { Helmet } from 'react-helmet-async';


// @mui
import { styled } from '@mui/material/styles';
import { Container, Typography, Divider } from '@mui/material';
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

    return (
        <>
            <Helmet>
                <title> New Password | Open Restaurant </title>
            </Helmet>

            <StyledRoot>

                <Container maxWidth="sm">
                    <StyledContent>
                        <Typography variant="h4" align='center'>
                            Create new password
                        </Typography>

                        <Typography variant="body5" sx={{ my: 5 }} align='center'>
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
