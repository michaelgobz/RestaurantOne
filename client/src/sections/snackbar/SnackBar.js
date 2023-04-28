import React from 'react';
import PropTypes from 'prop-types';
import { Alert, Snackbar } from '@mui/material';

SnackBar.propTypes = {
    message: PropTypes.string,
    severity: PropTypes.string,
};

export default function SnackBar({ message, severity }) {

    const [open, setOpen] = React.useState(false);

    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }

        setOpen(false);
    };

    return (
        <>
            <Snackbar
                anchorOrigin={{
                    vertical: 'bottom',
                    horizontal: 'left',
                }}
                open={open}
                autoHideDuration={6000}
                onClose={handleClose}

            />
            <Alert onClose={handleClose} severity={severity} sx={{ width: '100%' }}>
                {message}
            </Alert>
        </>
    );
}
