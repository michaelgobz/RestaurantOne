import * as React from 'react';
import { useNavigate } from 'react-router';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Paper from '@mui/material/Paper';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import Button from '@mui/material/Button';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import { createTheme } from '@mui/material/styles';
import ContactDetails from './ContactDetails';
import PaymentForm from './PaymentForm';
import Review from './Review';
import ThemeProvider from '../../theme'


function Copyright() {
  return (
    <Typography variant="body2" color="text.secondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="/">
        one restaurant
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const steps = ['Shipping address', 'Payment details', 'Review your order'];

function getStepContent(step) {
  switch (step) {
    case 0:
      return <ContactDetails />;
    case 1:
      return <PaymentForm />;
    case 2:
      return <Review />;
    default:
      throw new Error('Unknown step');
  }
}

const theme = createTheme();

export default function NewReservation() {

  const [activeStep, setActiveStep] = React.useState(0);

  const navigate = useNavigate()
  const HandleClick = () => {
    navigate('/')
  }

  const handleNext = () => {
    setActiveStep(activeStep + 1);
  };

  const handleBack = () => {
    setActiveStep(activeStep - 1);
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="sm" sx={{ mb: 4 }}>
        <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
          <Typography component="h1" variant="h4" align="center">
            Checkout
          </Typography>
          <Stepper activeStep={activeStep} sx={{ pt: 3, pb: 5 }}>
            {steps.map((label) => (
              <Step key={label}>
                <StepLabel>{label}</StepLabel>
              </Step>
            ))}
          </Stepper>
          {activeStep === steps.length ? (
            <>
              <Typography variant="h5" gutterBottom>
                Thank you for your order.
              </Typography>
              <Typography variant="subtitle1">
                Your order number is #2001539. We have emailed your order
                confirmation, and will send you an update when your order has
                shipped.
              </Typography>
              <Button
                  variant="contained"
                  onClick={HandleClick}
                  sx={{ mt: 3, ml: 1 }}
                >
            Get More
                </Button>
            </>
          ) : (
            <>
              {getStepContent(activeStep)}
              <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
                {activeStep !== 0 && (
                  <Button onClick={handleBack} sx={{ mt: 3, ml: 1 }}>
                    Back
                  </Button>
                )}

                <Button
                  variant="contained"
                  onClick={handleNext}
                  sx={{ mt: 3, ml: 1 }}
                >
                  {activeStep === steps.length - 1 ? 'Place order' : 'Next'}
                </Button>
              </Box>
            </>
          )}
        </Paper>
        <Copyright />
      </Container>
    </ThemeProvider>
  );
}