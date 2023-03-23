import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";



export default function DisplayMenu() {
    return (
        <>
            <Typography variant="h4" component="h1" gutterBottom>
                Dinner Menu
            </Typography>
            <Divider sx={{ my: 5 }} />
            <Typography variant="body3" gutterBottom>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed
                malesuada, nisl eget aliquam tincidunt, nunc elit aliquam erat,
                vitae aliquam nisl nunc eget lorem. Sed euismod, nisl nec
                tincidunt aliquam, nunc elit aliquam erat, vitae aliquam nisl
                nunc eget lorem. Sed euismod, nisl nec tincidunt aliquam, nunc
                elit aliquam erat, vitae aliquam nisl nunc eget lorem. Sed
                euismod, nisl nec tincidunt aliquam, nunc elit aliquam erat,
            </Typography>
            <Typography variant="h4" component="h1" gutterBottom>
                Lunch Menu
            </Typography>
            <Divider sx={{ my: 5 }} />
            <Typography variant="body3" gutterBottom>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed
                malesuada, nisl eget aliquam tincidunt, nunc elit aliquam erat,
                vitae aliquam nisl nunc eget lorem. Sed euismod, nisl nec
                tincidunt aliquam, nunc elit aliquam erat, vitae aliquam nisl
                nunc eget lorem. Sed euismod, nisl nec tincidunt aliquam, nunc
            </Typography>

        </>

    )
}