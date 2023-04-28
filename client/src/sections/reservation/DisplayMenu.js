import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";
import PropTypes from 'prop-types';



DisplayMenu.propTypes = {
    menus: PropTypes.array.isRequired
}


export default function DisplayMenu({ menus }) {
    return (
        <>
            {
                menus.map((menu) => 
                    (
                        <>
                            <Typography variant="h4" component="h1" gutterBottom>
                                {menu.name}
                            </Typography>
                            <Divider sx={{ my: 5 }} />
                            <Typography variant="body3" gutterBottom>
                                {menu.description}
                            </Typography>
                            <Divider sx={{ my: 5 }} />
                            {
                            menu.items.map((item) => (

                                        <>
                                            <Typography variant="body3" gutterBottom>
                                                {item.name}
                                            </Typography>
                                            <Typography variant="body3" gutterBottom>
                                                {item.description}
                                            </Typography>
                                            <Typography variant="body3" gutterBottom>
                                                {item.price}
                                            </Typography>
                                        </>
                                    )
                            )
                            }
                        </>
                    )
                )
            }

        </>

    )
}
