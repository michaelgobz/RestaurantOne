import * as React from 'react';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material';


export default function FindTable() {
  const [time, setTime] = React.useState('');
  const [occasion, setOccasion] = React.useState('');
  const [noOfPeople, setNoOfPeople] = React.useState(0);
  const [TableEnvironment, setTableEnvironment] = React.useState('');

  const handleChange = (event) => {
    setTime(event.target.value);
  };

  return (
    <>
      <Typography variant="h6" gutterBottom sx={{ my: 10 }}>
        Choose an Experience
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={6} sm={6}>

          <FormControl sx={{ m: 1, minWidth: 400 }} size="large">
            <InputLabel id="demo-select-small">Choose a Time</InputLabel>
            <Select
              labelId="demo-select-small"
              id="demo-select-small"
              value={time}
              label="Choose a Time"
              onChange={handleChange}
            >
              <MenuItem value={'11:30'}>11:30</MenuItem>
              <MenuItem value={'13:30'}>13:30</MenuItem>
              <MenuItem value={'18:00'}>18:00</MenuItem>
              <MenuItem value={'20:00'}>20:00</MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={12} sm={6}>
          <LocalizationProvider dateAdapter={AdapterDayjs}>
            <DatePicker
              label={'Choose a Date'}
              views={['year', 'month', 'day']}
            />
          </LocalizationProvider>
        </Grid>
        <Grid item xs={12}>
          <FormControl sx={{ m: 1, minWidth: 400 }} size="large">
            <InputLabel id="demo-select-small">Choose Occasion</InputLabel>
            <Select
              labelId="demo-select-small"
              id="demo-select-small"
              value={occasion}
              label="Choose Occasion"
              onChange={(event) => {
                setOccasion(event.target.value);
              }
              }
            >
              <MenuItem value={'break fast'}>Break fast</MenuItem>
              <MenuItem value={'dinner'}>Dinner</MenuItem>
              <MenuItem value={'date'}>Date</MenuItem>
              <MenuItem value={'lunch'}>Lunch</MenuItem>
              <MenuItem value={'family hangout'}>Family Hangout</MenuItem>
              <MenuItem value={'birthday'}>Birthday</MenuItem>
              <MenuItem value={'anniversary'}>Anniversary</MenuItem>
              <MenuItem value={'other'}>Other</MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={12}>
          <FormControl sx={{ m: 1, minWidth: 400 }} size="large">
            <InputLabel id="demo-select-small">Set number of people</InputLabel>
            <Select
              labelId="demo-select-small"
              id="demo-select-small"
              value={noOfPeople}
              label="Set number of people"
              onChange={(event) => {
                setNoOfPeople(event.target.value)
              }}
            >
              <MenuItem value={2}>2</MenuItem>
              <MenuItem value={3}>3</MenuItem>
              <MenuItem value={4}>3</MenuItem>
              <MenuItem value={5}>3</MenuItem>
              <MenuItem value={6}>6</MenuItem>
              <MenuItem value={7}>7</MenuItem>
              <MenuItem value={8}>8</MenuItem>
              <MenuItem value={9}>9</MenuItem>
              <MenuItem value={10}>10</MenuItem>
              <MenuItem value={11}>11</MenuItem>
              <MenuItem value={12}>12</MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={12}>
          <FormControl sx={{ m: 1, minWidth: 400 }} size="large">
            <InputLabel id="demo-select-small">Choose table environment</InputLabel>
            <Select
              labelId="demo-select-small"
              id="demo-select-small"
              value={TableEnvironment}
              label="Choose table environment"
              onChange={(event) => {
                setTableEnvironment(event.target.value)
              }}
            >
              <MenuItem value={'OutDoor'}>OutDoor</MenuItem>
              <MenuItem value={'InDoor'}>InDoor</MenuItem>
              <MenuItem value={'Window Adjustment'}>Window Adjustment</MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={12}>
          <FormControlLabel
            control={<Checkbox color="secondary" name="saveDetails" value="yes" />}
            label="I confirm the reservation details are correct"
          />
        </Grid>
      </Grid>
    </>
  );
}
