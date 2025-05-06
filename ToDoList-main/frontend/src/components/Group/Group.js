import Task from '../Task/Task'
import styles from './Group.css'


export default function Group() {
    return (
        <div className="group" style={styles}>
            group
            <Task />
            <Task />
        </div>
    )
}