function Card({task, onDelete}) {
    return (
        <div>
            <h3>{task.title}</h3>
            <button onClick={() => onDelete(task.id)}>x</button> 
            {/* <button onClick={onDelete(task.id)}>x</button> */}
        </div>
    );
}

export default Card;