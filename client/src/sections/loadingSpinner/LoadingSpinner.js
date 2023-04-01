import propTypes from 'prop-types';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import CircularProgress from '@mui/material/CircularProgress';


const LoadingSpinner = ({ text = 'loading...' }) => {
    (
        <>
            <Box display='flex' flexDirection='column' alignItems='center' mt={10}>
                <CircularProgress />
                <Typography variant='overline' sx={{ my: 2 }}>{text}</Typography>
            </Box>
        </>

    )
};

LoadingSpinner.propTypes = {
    text: propTypes.string,
};

export default LoadingSpinner;