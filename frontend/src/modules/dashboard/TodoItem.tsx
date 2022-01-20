import { FC } from "react";

const TodoItem: FC = () => {
    return (
        <div className="bg-primary-300 px-3 py-4 shadow-sm rounded">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores, deserunt
            atque modi, ratione odio facere eos laudantium quisquam, pariatur voluptates
            sit aut voluptatem dolorem vel maxime itaque laboriosam sequi earum?
        </div>
    );
};

TodoItem.displayName = "TodoItem";
export default TodoItem;
