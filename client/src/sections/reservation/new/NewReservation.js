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
import FindTable from './FindTable';
import SelectMenu from './SelectMenu';
import ContactDetails from './ContactDetails';
import PaymentForm from './PaymentForm';
import Review from './Review';
import ThemeProvider from '../../../theme'



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

const steps = ['Choose a Table','Add your details','Choose a Menu','Payment details', 'Review'];

function getStepContent(step, menuItems) {
  switch (step) {
    case 0:
      return <FindTable />;
    case 1:
      return <ContactDetails />;
    case 2:
      return <SelectMenu menuItems={menuItems} />;
    case 3:
      return <PaymentForm />;
    case 4:
      return <Review />;
    default:
      throw new Error('Unknown step');
  }
}

const theme = createTheme();

localStorage.setItem('newReservation', JSON.stringify([]))

export default function NewReservation() {

  const [menuItems, setMenuItems] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState(null);

  const api = `${process.env.REACT_APP_API}/dashboard/restaurants/${restaurantId}`;

  const requestOptions = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',

    },
  };

  // fetch restaurant menu items
  React.useEffect(() => {
    fetch(api, requestOptions).then((response) => {
      response.json().then((data) => {
        console.log(data.menus.items)
        setMenuItems(data.menus.items);
        setLoading(false);
      }
      ).catch((error) => {
        setError(error);
        setLoading(false);
        console.log(error)
      });
    });
  }, []);

  const [activeStep, setActiveStep] = React.useState(0);
  const restaurantId = useParams().restaurantId;

  const navigate = useNavigate()
  const HandleClick = () => {
    navigate('/customers/restaurants/')
  }

  const handleNext = () => {
    setActiveStep(activeStep + 1);
  };

  const handleBack = () => {
    setActiveStep(activeStep - 1);
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="lm" maxLength="lm" sx={{ mb: 4 }}>
        <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
          <Typography component="h1" variant="h4" align="center">
            Reserve A Table
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
                Your Reservation Has been Made
              </Typography>
              <Typography variant="subtitle1">
                Thank you for your reservation. We will contact you shortly to confirm your reservation.
              </Typography>
              <Button
                  variant="contained"
                  onClick={HandleClick}
                  sx={{ mt: 3, ml: 1 }}
                >
                Make another reservation

                </Button>
            </>
          ) : (
            <>
                {getStepContent(activeStep, menuItems)}
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