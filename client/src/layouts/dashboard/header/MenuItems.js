import { useState } from 'react'
import { useNavigate } from 'react-router';// import useState hook from react
import { Tabs, Tab } from '@mui/material'

export function MenuItems() {

    const [value, setValue] = useState('one');
    const navigate = useNavigate();

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
                    }}
                    label="Order" />
                <Tab value="two"
                    onFocus={() => {
                        setValue("two")
                        navigate("/reservations")
                    }}
                    label="Reservation" />
            </Tabs>
        </>
    );
}