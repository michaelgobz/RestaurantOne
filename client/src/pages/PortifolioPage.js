import { Helmet } from 'react-helmet-async';
import { useEffect, useState } from 'react';
// @mui
import { Container, Stack, Typography } from '@mui/material';

export default function PortfolioPage() {
    // describe the portfolio page
    return (
        <>
            <Helmet>
                <title> Portfolio | Open Restaurant </title>
            </Helmet>
            <Container>
                <Typography variant="h4" sx={{ mb: 5 }}>
                    Portfolio
                </Typography>
                <Typography variant="h6" sx={{ mb: 5 }}>
                    This is the portfolio page
                </Typography>
            </Container>
        </>
    );

}