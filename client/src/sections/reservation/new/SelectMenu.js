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
      <Typography variant="h6" gutterBottom sx={{ my: 10 }}>
        Choose Menu
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6}>
          <div>
            <FormControl sx={{ m: 1, width: 400 }}>
              <InputLabel id="demo-multiple-checkbox-label">Menus</InputLabel>
              <Select
                labelId="demo-multiple-checkbox-label"
                id="demo-multiple-checkbox"
                multiple
                label="Select Menu Item"
                value={itemName}
                onChange={handleChange}
                input={<OutlinedInput label="Menus" />}
                renderValue={(selected) => selected}
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
