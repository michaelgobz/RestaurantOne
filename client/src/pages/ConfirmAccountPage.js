import { Helmet } from 'react-helmet-async';

// @mui
import { styled } from '@mui/material/styles';
import { Container, Typography, Divider } from '@mui/material';
// hooks
// import useResponsive from '../hooks/useResponsive';

// components

import ConfirmAccount from '../sections/auth/utils/ConfirmAccount';


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

export default function ConfirmAccountPage() {

    // const mdUp = useResponsive('up', 'md')

    return (
        <>
            <Helmet>
                <title> ConfirmAccount | Open Restaurant </title>
            </Helmet>

            <StyledRoot>

                <Container maxWidth="sm">
                    <StyledContent>
                        <Typography variant="h4" gutterBottom align='center'>
                            Confirm Account
                        </Typography>

                        <Typography variant="body5" sx={{ my: 5 }} align='center'>
                            Enter the token you received in your email to verify account
                        </Typography>

                        <Divider sx={{ my: 3 }} />

                        <ConfirmAccount />

                        <Divider sx={{ my: 3 }} />
                    </StyledContent>
                </Container>
            </StyledRoot>
        </>
    );
}
