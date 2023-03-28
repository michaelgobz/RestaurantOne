import { useParams } from 'react-router';
import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Grid from '@mui/material/Grid';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import ListItemText from '@mui/material/ListItemText';
import Select from '@mui/material/Select';

import Typography from '@mui/material/Typography';
import { constant } from 'lodash';

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250,
    },
  },
};

// menu items go here 

const MenuItems = [
  'Oliver Hansen',
  'Van Henry',
  'April Tucker',
  'Ralph Hubbard',
  'Omar Alexander',
  'Carlos Abbott',
  'Miriam Wagner',
  'Bradley Wilkerson',
  'Virginia Andrews',
  'Kelly Snyder',
];

SelectMenu.propTypes = {
  MenuItems: PropTypes.array.isRequired,
};


export default function SelectMenu({ MenuItems }) {

  const [itemName, setItemName] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [setMenuItems] = useState([]);

  const restaurantId = useParams().restaurantId;
  const url = `${process.env.REACT_APP_API}/dashboard/restaurants/${restaurantId}`
  const requestOptions = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  };

  // get menu items from restaurantId
  // const [MenuItems, setMenuItems] = React.useState([]);
  useEffect(() => {
    fetch(url, requestOptions).then((response) => {
      response.json().then((data) => {
        console.log(data.restaurant.menus)
        setMenuItems(data.restaurant.menus);
        setLoading(false);
      }
      ).catch((error) => {
        setError(error);
        setLoading(false);
        console.log(error)
      });
    });

  }, []);


  const handleChange = (event) => {
    const {
      target: { value },
    } = event;
    setItemName(
      // On autofill we get a stringified value.
      typeof value === 'string' ? value : '',
    );
  };


  return (
    <>
      <Typography variant="h6" gutterBottom>
        Choose Menu
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6}>
          <div>
            <FormControl sx={{ m: 1, width: 400 }}>
              <InputLabel id="demo-multiple-checkbox-label">Tag</InputLabel>
              <Select
                labelId="demo-multiple-checkbox-label"
                id="demo-multiple-checkbox"
                multiple
                label="Select Menu Item"
                value={itemName}
                onChange={handleChange}
                input={<OutlinedInput label="Tag" />}
                renderValue={(selected) => selected.join(', ')}
                MenuProps={MenuProps}
              >
                {MenuItems.map((item) => (
                  <MenuItem key={item} value={item}>
                    <ListItemText primary={item} />
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          </div>
        </Grid>

      </Grid>
    </>
  );
}
