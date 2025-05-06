import styles from './LeftMenu.css'
import React, { useState, useEffect } from 'react';


export default function LeftMenu() {

    const [tables, setTables] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/todo/table', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage["access"]
            },
        })
            .then(res => res.json())
            .then((data) => {
                setTables(data["tables"]);
            });
    }, []); 

    return (
        <aside style={styles} id="sidebar">
            sidebar test
            {tables.length > 0 && (
                <ul>
                    {tables.map(table => (
                        <li key={table.id}><a href={`${"http://127.0.0.1:3000/todo/table/"}${table.id}`}>{table.name}</a></li>
                    ))}
                </ul>
            )}
        </aside>
    );
}