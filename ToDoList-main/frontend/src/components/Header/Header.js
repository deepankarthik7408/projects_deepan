import styles from './Header.css'


export default function Header() {
    return (
        <header style={styles}>
            <p className="logo">header</p>
            <a href='http://127.0.0.1:3000/account.html'>
                <p className="account">
                    account
                </p>
            </a>
        </header>
    );
}