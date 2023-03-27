import Typography from "@mui/material/Typography";
import PropTypes from 'prop-types';


DisplayDescription.propTypes = {
    description: PropTypes.string.isRequired
}


export default function DisplayDescription({ description }) {
    return (
        <>

            <Typography variant="body3" gutterBottom>
                {description}
            </Typography>


        </>

    )
}