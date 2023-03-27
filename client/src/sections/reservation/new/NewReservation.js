import * as React from 'react';
import { useNavigate, useParams, useEffect } from 'react-router';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Paper from '@mui/material/Paper';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import Button from '@mui/material/Button';
import Link from '@mui/material/Link';
import Modal from '@mui/joy/Modal';
import ModalClose from '@mui/joy/ModalClose';
import ModalDialog from '@mui/joy/ModalDialog';
import Typography from '@mui/material/Typography';
import { createTheme } from '@mui/material/styles';
import FindTable from './FindTable';
import SelectMenu from './SelectMenu';
import ContactDetails from './ContactDetails';
import PaymentForm from './PaymentForm';
import Review from './Review';
import ThemeProvider from '../../../theme';


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

const steps = ['Choose a Table', 'Add your details', 'Choose a Menu', 'Payment details', 'Review'];

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
  const [activeStep, setActiveStep] = React.useState(0);
  const [open, setOpen] = React.useState(false);
  const [variant, setVariant] = React.useState('soft');
  const restaurantId = useParams().restaurantId;

  const handleClose = () => {
    setOpen(false);
  };

  const api = `${process.env.REACT_APP_API}/dashboard/restaurants/${restaurantId}`;
  const reservationUrl = `${process.env.REACT_APP_API}/dashboard/reservations/${sessionStorage.getItem('user')}/${restaurantId}`

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


  const navigate = useNavigate()

  const HandleClick = () => {
    if (sessionStorage.getItem('token') === null) {
      navigate('/auth/login')
    } else {
      CreateReservation()
      navigate('/customers/restaurants/')
    }
  }

  const CreateReservation = () => {
    const reservation = JSON.parse(localStorage.getItem('newReservation'))
    useEffect(() => {

      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        },
        body: JSON.stringify(reservation)
      };
      fetch(reservationUrl
        , requestOptions)
        .then(response => response.json().then(data => {
          if (response.status === 200) {
            console.log(data.message)
            // display a model to show the user that the reservation was successful
            return (
              <Model open={open} onClose={() => setVariant(undefined)}>
                <ModalDialog
                  aria-labelledby="variant-modal-title"
                  aria-describedby="variant-modal-description"
                  variant={variant}
                >
                  <ModalClose />
                  <Typography id="variant-modal-title" component="h2" level="inherit">
                    New Reservation
                  </Typography>
                  <Typography id="variant-modal-description" textColor="inherit">
                    {data.message}
                  </Typography>
                </ModalDialog>
              </Model>
            )
          } else {
            console.log('some thing went wrong')
          }
        })).catch(error => {
          console.log(error)
        }
        )
    }, [])
  }


  const handleNext = () => {
    setActiveStep(activeStep + 1);
  };

  const handleBack = () => {
    setActiveStep(activeStep - 1);
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="ls" maxLength="ls" sx={{ mb: 4 }}>
        <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
          <Typography component="h1" variant="h4" align="center">
            Reserve A Table
          </Typography>
          <Stepper activeStep={activeStep} sx={{ pt: 2, pb: 1 }}>
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