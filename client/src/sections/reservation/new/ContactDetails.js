import * as React from 'react';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { last } from 'lodash';

export default function ContactDetails() {

  const [email, setEmail] = React.useState('');
  const [phoneNumber, setPhoneNumber] = React.useState('');
  const [timeOfArrival, setTimeOfArrival] = React.useState('');
  const [firstName, setFirstName] = React.useState('');
  const [lastName, setLastName] = React.useState('');

  return (
    <>
      <Typography variant="h6" gutterBottom>
        ContactDetails
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6}>
          <TextField
            required
            id="firstName"
            name="firstName"
            label="First name"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            fullWidth
            autoComplete="given-name"
            variant="standard"
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            required
            id="lastName"
            name="lastName"
            label="Last name"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)} 
            fullWidth
            autoComplete="family-name"
            variant="standard"
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            required
            id="email"
            name="email"
            label="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            variant="standard"
            fullWidth />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            required
            id="phone"
            name="phone Number"
            label="Phone Number"
            value={phoneNumber}
            variant="standard"
            onChange={(e) => setPhoneNumber(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            required
            id="time of arrival"
            name="time of arrival"
            label="Time of Arrival"
            value={timeOfArrival}
            variant="standard"
            onChange={(e) => setTimeOfArrival(e.target.value)}
            fullWidth
          />
        </Grid>

        <Grid item xs={12}>
          <FormControlLabel
            control={<Checkbox color="secondary" name="saveAddress" value="yes" />}
            label="I confirm the details are correct and concent to being contacted by the restaurant"
          />
        </Grid>
      </Grid>
    </>
  );
}
