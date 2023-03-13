import { Tabs, Tab } from '@mui/material'

export function MenuItems() {

    let value = "one" // default value
    const setValue = (val) => {
        value = val
    }
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
                    }}
                    label="Reservation" />
            </Tabs>
        </>
    );
}