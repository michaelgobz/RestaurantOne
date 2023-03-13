
import { Pagination } from '@mui/material';

export function PaginationComponent() {


    return (
        <>
            <Pagination count={10} hidePrevButton hideNextButton sx={{
                mt: 5,
                mr: 0,
                display: 'flex',
            }} />
        </>
    )
}   