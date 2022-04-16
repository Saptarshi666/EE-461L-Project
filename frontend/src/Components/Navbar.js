/*
    from the video link in the homework file
*/
import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';
// import Button from '@mui/material/Button';
// import BabyChangingStation from '@mui/icons-material/BabyChangingStation';

function Navbar() {
    const [click, setClick] = useState(false);
    const [button, setButton] = useState(true)

    const handleClick = () => setClick(!click);
    const closeMobileMenu = () => setClick(false);

    const showButton = () => {
        if(window.innerWidth <= 960){
            setButton(false);
        } else {
            setButton(true);
        }
    };

    window.addEventListener('resize', showButton);

    return (
        <>
            <nav className="navbar">
                <div className="navbar-container">
                    <li className='navbar-logo'>
                        <Link to='/' className='navbar-logo' onCLick={closeMobileMenu}>
                            {/* <BabyChangingStation fontSize='large'/>  */}
                        </Link>
                        <Link to='/' className='navbar-logo' onCLick={closeMobileMenu}>
                            MVP
                        </Link>
                    </li>
                    <div className='menu-icon' onClick={handleClick}>
                        {/* <BabyChangingStation fontSize='large'/><i className={click ? 'fas-fa-times' : 'fas fa-bars'} /> */}
                    </div>
                    <ul className={click ? 'nav-menu active' :'nav-menu'}>
                        <li className='nav-item'>
                            <Link to='/Logout' className='nav-links' onCLick={closeMobileMenu}>
                                Home
                            </Link>
                        </li>
                        <li className='nav-item'>
                            <Link to='/projectpage' className='nav-links' onCLick={closeMobileMenu}>
                                Projects
                            </Link>
                        </li>
                        <li className='nav-item'>
                            <Link to='/SetsDatas' className='nav-links' onCLick={closeMobileMenu}>
                                Datasets
                            </Link>
                        </li>
                        <li className='nav-item'>
                            <Link to='/Logout' className='nav-links-mobile' onCLick={closeMobileMenu}>
                                Log Out
                            </Link>
                        </li>
                    </ul>
                    {/* {button && <Button variant="contained">SIGN UP</Button>} */}
                </div>
            </nav>
        </>
    )
}

export default Navbar