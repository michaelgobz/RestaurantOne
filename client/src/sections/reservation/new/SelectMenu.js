import * as React from 'react';
import { useParams } from 'react-router';
import Grid from '@mui/material/Grid';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import ListItemText from '@mui/material/ListItemText';
import Select from '@mui/material/Select';
import Checkbox from '@mui/material/Checkbox';
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


export default function SelectMenu() {
  const [name, setName] = React.useState([]);
  const { restaurantId } = useParams('restaurantId');
  const [menuNames, setMenuNames] = React.useState([]);
  

  const api = `${process.env.REACT_APP_API}/dashboard/restaurants/${restaurantId}`;


  React.useEffect(() => {

    const requestOptions = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',

      },
    };


    let menuItems = [];
    fetch(api, requestOptions).then((response) => {
      response.json().then((data) => {
        console.log(data.restaurant.menus)
        menuItems = (data.restaurant.menus);

        const items = menuItems.map((item) =>
          item.items
        )
        console.log(items)

        const menuNames = items.map((item) =>
          item.map((item) =>
            item.name
          )
        )
        const flattened = menuNames.flat()
        setMenuNames(flattened)
      }
      ).catch((error) => {
        console.log(error)
      });
    });
  }, [api]);


  const handleChange = (event) => {
    const {
      target: { value },
    } = event;
    setName(
      // On autofill we get a stringified value.
      typeof value === 'string' ? value.split(',') : value,
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
            <FormControl sx={{ m: 1, width: 300 }}>
              <InputLabel id="demo-multiple-checkbox-label">Menus</InputLabel>
              <Select
                labelId="demo-multiple-checkbox-label"
                id="demo-multiple-checkbox"
                multiple
                label="Select Menu Item"
                value={name}
                onChange={handleChange}
                input={<OutlinedInput label="Tag" />}
                renderValue={(selected) => selected.join(', ')}
                MenuProps={MenuProps}
              >
                {menuNames.map((name) => (
                  <MenuItem key={Math.random(10)} value={name}>
                    <Checkbox checked={menuNames.indexOf(name) > 1} />
                    <ListItemText primary={name} />
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
