import { useState } from 'react'
import { redirect, useNavigate } from 'react-router';// import useState hook from react
import { Tabs, Tab } from '@mui/material'

export function MenuItems() {

    const navigator = useNavigate();

    const [value, setValue] = useState('one');

    const handleChange = () => {
        setValue(value)
    }
    return (
        <>
            <Tabs
                value={value}
                onChange={handleChange}
                variant="scrollable"
                textColor="secondary"
                indicatorColor="secondary"
                aria-label="secondary tabs example"
            >
                <Tab value="one"

                    onFocus={() => {
                        setValue("one")
                        navigator("customer/products")
                    }}
                    label="New Order" />
                <Tab value="two"
                    onFocus={() => {
                        setValue("two")
                        navigator("customer/reservations")
                    }}
                    label="New Reservation" />
            </Tabs>
        </>
    );
}