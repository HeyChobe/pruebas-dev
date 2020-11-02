import Card from '../components/card'

const List = ({tasks, onDelete}) => { //Se pueden traer las tareas así
    //También sin las llaves en los parámetros
    //const {tasks} = props;
    return(
        <div>
            {tasks.map(task => (
                <Card key={task.id} task={task} onDelete={onDelete}/>
            ))}
        </div>
    );
}

export default List;